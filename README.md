# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 444
- HTTP: 90 alive / 77 gold
- HTTPS: 97 alive / 31 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 190 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47349
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
