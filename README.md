# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 399
- HTTP: 198 alive / 82 gold
- HTTPS: 157 alive / 30 gold
- SOCKS4: 203 alive / 147 gold
- SOCKS5: 218 alive / 140 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31899
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
