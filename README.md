# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 440
- HTTP: 119 alive / 81 gold
- HTTPS: 67 alive / 30 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44581
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
