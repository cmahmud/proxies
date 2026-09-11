# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 453
- HTTP: 102 alive / 86 gold
- HTTPS: 48 alive / 30 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 190 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49189
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
