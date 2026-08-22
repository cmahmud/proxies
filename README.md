# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 398
- HTTP: 248 alive / 90 gold
- HTTPS: 173 alive / 30 gold
- SOCKS4: 200 alive / 141 gold
- SOCKS5: 213 alive / 137 gold

## Historical pool

- Discovered: 163259
- Ever alive: 31779
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
