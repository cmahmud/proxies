# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 402
- HTTP: 150 alive / 75 gold
- HTTPS: 176 alive / 25 gold
- SOCKS4: 163 alive / 147 gold
- SOCKS5: 183 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40022
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
