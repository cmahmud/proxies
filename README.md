# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 398
- HTTP: 230 alive / 88 gold
- HTTPS: 116 alive / 21 gold
- SOCKS4: 201 alive / 137 gold
- SOCKS5: 231 alive / 152 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29758
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
