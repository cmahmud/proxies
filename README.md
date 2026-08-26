# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 385
- HTTP: 111 alive / 68 gold
- HTTPS: 48 alive / 17 gold
- SOCKS4: 159 alive / 143 gold
- SOCKS5: 173 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38919
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
