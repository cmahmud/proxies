# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 399
- HTTP: 142 alive / 69 gold
- HTTPS: 62 alive / 14 gold
- SOCKS4: 181 alive / 155 gold
- SOCKS5: 204 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33290
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
