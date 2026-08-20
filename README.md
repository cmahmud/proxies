# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 392
- HTTP: 241 alive / 82 gold
- HTTPS: 184 alive / 23 gold
- SOCKS4: 199 alive / 137 gold
- SOCKS5: 212 alive / 150 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27167
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
