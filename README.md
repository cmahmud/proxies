# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 444
- HTTP: 109 alive / 79 gold
- HTTPS: 96 alive / 32 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47008
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
