# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 344
- HTTP: 103 alive / 38 gold
- HTTPS: 48 alive / 10 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 172 alive / 144 gold

## Historical pool

- Discovered: 171048
- Ever alive: 32856
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
