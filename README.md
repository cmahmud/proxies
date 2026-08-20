# SyndProxy private pool

## Current pool

- Alive now: 1304
- Gold now: 575
- HTTP: 438 alive / 177 gold
- HTTPS: 342 alive / 93 gold
- SOCKS4: 236 alive / 141 gold
- SOCKS5: 288 alive / 164 gold

## Historical pool

- Discovered: 138941
- Ever alive: 23193
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
