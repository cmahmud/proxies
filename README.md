# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 433
- HTTP: 116 alive / 85 gold
- HTTPS: 57 alive / 29 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49433
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
