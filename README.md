# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 445
- HTTP: 138 alive / 77 gold
- HTTPS: 101 alive / 34 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 203 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45372
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
