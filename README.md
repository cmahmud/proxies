# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 404
- HTTP: 197 alive / 72 gold
- HTTPS: 66 alive / 14 gold
- SOCKS4: 187 alive / 155 gold
- SOCKS5: 213 alive / 163 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33297
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
