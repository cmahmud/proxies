# SyndProxy private pool

## Current pool

- Alive now: 652
- Gold now: 384
- HTTP: 156 alive / 70 gold
- HTTPS: 92 alive / 16 gold
- SOCKS4: 198 alive / 154 gold
- SOCKS5: 206 alive / 144 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25697
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
