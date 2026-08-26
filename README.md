# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 408
- HTTP: 105 alive / 65 gold
- HTTPS: 97 alive / 15 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38076
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
