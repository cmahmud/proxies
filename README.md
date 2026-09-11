# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 296
- HTTP: 154 alive / 73 gold
- HTTPS: 167 alive / 35 gold
- SOCKS4: 53 alive / 52 gold
- SOCKS5: 138 alive / 136 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48482
- Ever gold: 1541

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
