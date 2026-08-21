# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 404
- HTTP: 272 alive / 96 gold
- HTTPS: 230 alive / 27 gold
- SOCKS4: 226 alive / 155 gold
- SOCKS5: 211 alive / 126 gold

## Historical pool

- Discovered: 160982
- Ever alive: 30860
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
