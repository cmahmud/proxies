# SyndProxy private pool

## Current pool

- Alive now: 797
- Gold now: 395
- HTTP: 205 alive / 77 gold
- HTTPS: 157 alive / 21 gold
- SOCKS4: 231 alive / 150 gold
- SOCKS5: 204 alive / 147 gold

## Historical pool

- Discovered: 150517
- Ever alive: 27049
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
