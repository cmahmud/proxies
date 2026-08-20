# SyndProxy private pool

## Current pool

- Alive now: 757
- Gold now: 387
- HTTP: 171 alive / 73 gold
- HTTPS: 157 alive / 19 gold
- SOCKS4: 226 alive / 150 gold
- SOCKS5: 203 alive / 145 gold

## Historical pool

- Discovered: 150517
- Ever alive: 27047
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
