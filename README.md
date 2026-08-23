# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 199
- HTTP: 176 alive / 43 gold
- HTTPS: 50 alive / 6 gold
- SOCKS4: 110 alive / 66 gold
- SOCKS5: 155 alive / 84 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32732
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
