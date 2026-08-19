# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 488
- HTTP: 376 alive / 128 gold
- HTTPS: 258 alive / 84 gold
- SOCKS4: 192 alive / 123 gold
- SOCKS5: 229 alive / 153 gold

## Historical pool

- Discovered: 119650
- Ever alive: 17860
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
