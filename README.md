# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 371
- HTTP: 97 alive / 47 gold
- HTTPS: 32 alive / 12 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 186 alive / 158 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33025
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
