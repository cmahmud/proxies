# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 389
- HTTP: 84 alive / 47 gold
- HTTPS: 65 alive / 15 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41612
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
