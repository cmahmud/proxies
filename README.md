# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 471
- HTTP: 151 alive / 100 gold
- HTTPS: 111 alive / 35 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45126
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
