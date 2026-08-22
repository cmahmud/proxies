# SyndProxy private pool

## Current pool

- Alive now: 786
- Gold now: 395
- HTTP: 205 alive / 89 gold
- HTTPS: 153 alive / 30 gold
- SOCKS4: 203 alive / 118 gold
- SOCKS5: 225 alive / 158 gold

## Historical pool

- Discovered: 163856
- Ever alive: 31951
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
