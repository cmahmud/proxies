# SyndProxy private pool

## Current pool

- Alive now: 1386
- Gold now: 592
- HTTP: 551 alive / 183 gold
- HTTPS: 354 alive / 111 gold
- SOCKS4: 247 alive / 143 gold
- SOCKS5: 234 alive / 155 gold

## Historical pool

- Discovered: 125593
- Ever alive: 19553
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
