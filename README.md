# SyndProxy validated proxy pool

## Current pool

- Alive now: 697
- Gold now: 466
- HTTP: 169 alive / 92 gold
- HTTPS: 135 alive / 37 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 221 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45302
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
