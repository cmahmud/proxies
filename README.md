# SyndProxy private pool

## Current pool

- Alive now: 640
- Gold now: 385
- HTTP: 143 alive / 67 gold
- HTTPS: 93 alive / 19 gold
- SOCKS4: 195 alive / 154 gold
- SOCKS5: 209 alive / 145 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25697
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
