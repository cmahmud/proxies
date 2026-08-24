# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 404
- HTTP: 183 alive / 72 gold
- HTTPS: 84 alive / 15 gold
- SOCKS4: 189 alive / 155 gold
- SOCKS5: 206 alive / 162 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33302
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
