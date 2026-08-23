# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 350
- HTTP: 114 alive / 42 gold
- HTTPS: 76 alive / 12 gold
- SOCKS4: 158 alive / 153 gold
- SOCKS5: 177 alive / 143 gold

## Historical pool

- Discovered: 171037
- Ever alive: 32810
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
