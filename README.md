# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 402
- HTTP: 108 alive / 66 gold
- HTTPS: 51 alive / 17 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38945
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
