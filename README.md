# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 420
- HTTP: 108 alive / 76 gold
- HTTPS: 51 alive / 18 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44487
- Ever gold: 1402

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
