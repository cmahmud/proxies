# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 410
- HTTP: 101 alive / 61 gold
- HTTPS: 92 alive / 15 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 199 alive / 173 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38190
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
