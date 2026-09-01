# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 430
- HTTP: 93 alive / 72 gold
- HTTPS: 96 alive / 30 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47318
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
