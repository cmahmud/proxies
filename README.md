# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 392
- HTTP: 306 alive / 81 gold
- HTTPS: 186 alive / 22 gold
- SOCKS4: 187 alive / 125 gold
- SOCKS5: 232 alive / 164 gold

## Historical pool

- Discovered: 151041
- Ever alive: 27128
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
