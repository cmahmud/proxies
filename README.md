# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 442
- HTTP: 123 alive / 79 gold
- HTTPS: 140 alive / 33 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44714
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
