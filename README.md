# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 451
- HTTP: 143 alive / 82 gold
- HTTPS: 105 alive / 34 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 221 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45436
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
