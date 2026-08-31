# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 480
- HTTP: 170 alive / 101 gold
- HTTPS: 136 alive / 42 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45236
- Ever gold: 1427

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
