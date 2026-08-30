# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 420
- HTTP: 110 alive / 72 gold
- HTTPS: 47 alive / 21 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44509
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
