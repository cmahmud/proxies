# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 479
- HTTP: 156 alive / 106 gold
- HTTPS: 142 alive / 37 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45230
- Ever gold: 1427

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
