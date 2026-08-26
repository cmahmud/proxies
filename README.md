# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 395
- HTTP: 144 alive / 73 gold
- HTTPS: 178 alive / 22 gold
- SOCKS4: 165 alive / 147 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40052
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
