# SyndProxy validated proxy pool

## Current pool

- Alive now: 712
- Gold now: 457
- HTTP: 170 alive / 87 gold
- HTTPS: 125 alive / 36 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 235 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45331
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
