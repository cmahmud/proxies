# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 320
- HTTP: 272 alive / 59 gold
- HTTPS: 185 alive / 13 gold
- SOCKS4: 194 alive / 126 gold
- SOCKS5: 198 alive / 122 gold

## Historical pool

- Discovered: 129244
- Ever alive: 20047
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
