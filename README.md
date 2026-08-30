# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 471
- HTTP: 136 alive / 95 gold
- HTTPS: 111 alive / 42 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 200 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44915
- Ever gold: 1418

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
