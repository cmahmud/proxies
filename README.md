# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 375
- HTTP: 84 alive / 46 gold
- HTTPS: 47 alive / 13 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 195 alive / 161 gold

## Historical pool

- Discovered: 172309
- Ever alive: 32964
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
