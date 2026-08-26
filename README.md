# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 415
- HTTP: 100 alive / 68 gold
- HTTPS: 90 alive / 18 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37826
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
