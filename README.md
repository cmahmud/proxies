# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 370
- HTTP: 190 alive / 69 gold
- HTTPS: 165 alive / 22 gold
- SOCKS4: 196 alive / 134 gold
- SOCKS5: 200 alive / 145 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26653
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
