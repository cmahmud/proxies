# SyndProxy private pool

## Current pool

- Alive now: 745
- Gold now: 333
- HTTP: 241 alive / 83 gold
- HTTPS: 136 alive / 21 gold
- SOCKS4: 168 alive / 103 gold
- SOCKS5: 200 alive / 126 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29769
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
