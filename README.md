# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 380
- HTTP: 130 alive / 65 gold
- HTTPS: 173 alive / 20 gold
- SOCKS4: 159 alive / 146 gold
- SOCKS5: 176 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39682
- Ever gold: 1300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
