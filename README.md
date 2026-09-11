# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 396
- HTTP: 98 alive / 68 gold
- HTTPS: 39 alive / 20 gold
- SOCKS4: 161 alive / 135 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48765
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
