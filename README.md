# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 464
- HTTP: 156 alive / 97 gold
- HTTPS: 134 alive / 35 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45170
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
