# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 440
- HTTP: 123 alive / 79 gold
- HTTPS: 104 alive / 32 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 194 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44628
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
